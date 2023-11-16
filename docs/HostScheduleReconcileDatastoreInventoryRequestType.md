# HostScheduleReconcileDatastoreInventoryRequestType

The parameters of *HostVStorageObjectManager.HostScheduleReconcileDatastoreInventory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_schedule_reconcile_datastore_inventory_request_type import HostScheduleReconcileDatastoreInventoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostScheduleReconcileDatastoreInventoryRequestType from a JSON string
host_schedule_reconcile_datastore_inventory_request_type_instance = HostScheduleReconcileDatastoreInventoryRequestType.from_json(json)
# print the JSON string representation of the object
print HostScheduleReconcileDatastoreInventoryRequestType.to_json()

# convert the object into a dict
host_schedule_reconcile_datastore_inventory_request_type_dict = host_schedule_reconcile_datastore_inventory_request_type_instance.to_dict()
# create an instance of HostScheduleReconcileDatastoreInventoryRequestType from a dict
host_schedule_reconcile_datastore_inventory_request_type_form_dict = host_schedule_reconcile_datastore_inventory_request_type.from_dict(host_schedule_reconcile_datastore_inventory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


