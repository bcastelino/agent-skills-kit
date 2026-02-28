# Temporal Python Pro Implementation Playbook

Detailed patterns and examples for Temporal workflow orchestration with the Python SDK.

## Workflow Patterns

### Basic Workflow
```python
from temporalio import workflow
from temporalio.common import RetryPolicy
from datetime import timedelta

@workflow.defn
class OrderWorkflow:
    @workflow.run
    async def run(self, order_id: str) -> str:
        result = await workflow.execute_activity(
            validate_order,
            order_id,
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(maximum_attempts=3),
        )
        await workflow.execute_activity(
            process_payment,
            order_id,
            start_to_close_timeout=timedelta(minutes=5),
        )
        await workflow.execute_activity(
            send_confirmation,
            order_id,
            start_to_close_timeout=timedelta(seconds=30),
        )
        return f"Order {order_id} completed"
```

### Activity Definitions
```python
from temporalio import activity

@activity.defn
async def validate_order(order_id: str) -> dict:
    order = await db.get_order(order_id)
    if not order:
        raise ApplicationError(f"Order {order_id} not found")
    return {"valid": True, "total": order.total}

@activity.defn
async def process_payment(order_id: str) -> str:
    result = await payment_gateway.charge(order_id)
    return result.transaction_id
```

## Worker Setup

```python
from temporalio.client import Client
from temporalio.worker import Worker

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="order-queue",
        workflows=[OrderWorkflow],
        activities=[validate_order, process_payment, send_confirmation],
    )
    await worker.run()
```

## Advanced Patterns

### Saga Pattern (Compensation)
```python
@workflow.defn
class SagaWorkflow:
    @workflow.run
    async def run(self, data: dict) -> str:
        compensations = []
        try:
            await workflow.execute_activity(reserve_inventory, data)
            compensations.append(cancel_inventory_reservation)
            await workflow.execute_activity(charge_payment, data)
            compensations.append(refund_payment)
            await workflow.execute_activity(ship_order, data)
            return "Success"
        except Exception:
            for compensation in reversed(compensations):
                await workflow.execute_activity(compensation, data)
            raise
```

### Signals and Queries
```python
@workflow.defn
class ApprovalWorkflow:
    def __init__(self):
        self.approved = False

    @workflow.signal
    async def approve(self):
        self.approved = True

    @workflow.query
    def status(self) -> str:
        return "approved" if self.approved else "pending"

    @workflow.run
    async def run(self) -> str:
        await workflow.wait_condition(lambda: self.approved)
        return "Approved and processed"
```

## Testing

```python
from temporalio.testing import WorkflowEnvironment

async def test_order_workflow():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue="test-queue",
            workflows=[OrderWorkflow],
            activities=[validate_order, process_payment, send_confirmation],
        ):
            result = await env.client.execute_workflow(
                OrderWorkflow.run,
                "order-123",
                id="test-wf",
                task_queue="test-queue",
            )
            assert result == "Order order-123 completed"
```
