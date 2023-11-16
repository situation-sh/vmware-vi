# ScheduleReconcileDatastoreInventoryRequestType

The parameters of *VcenterVStorageObjectManager.ScheduleReconcileDatastoreInventory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.schedule_reconcile_datastore_inventory_request_type import ScheduleReconcileDatastoreInventoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleReconcileDatastoreInventoryRequestType from a JSON string
schedule_reconcile_datastore_inventory_request_type_instance = ScheduleReconcileDatastoreInventoryRequestType.from_json(json)
# print the JSON string representation of the object
print ScheduleReconcileDatastoreInventoryRequestType.to_json()

# convert the object into a dict
schedule_reconcile_datastore_inventory_request_type_dict = schedule_reconcile_datastore_inventory_request_type_instance.to_dict()
# create an instance of ScheduleReconcileDatastoreInventoryRequestType from a dict
schedule_reconcile_datastore_inventory_request_type_form_dict = schedule_reconcile_datastore_inventory_request_type.from_dict(schedule_reconcile_datastore_inventory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


