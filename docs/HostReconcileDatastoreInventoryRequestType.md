# HostReconcileDatastoreInventoryRequestType

The parameters of *HostVStorageObjectManager.HostReconcileDatastoreInventory_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_reconcile_datastore_inventory_request_type import HostReconcileDatastoreInventoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostReconcileDatastoreInventoryRequestType from a JSON string
host_reconcile_datastore_inventory_request_type_instance = HostReconcileDatastoreInventoryRequestType.from_json(json)
# print the JSON string representation of the object
print HostReconcileDatastoreInventoryRequestType.to_json()

# convert the object into a dict
host_reconcile_datastore_inventory_request_type_dict = host_reconcile_datastore_inventory_request_type_instance.to_dict()
# create an instance of HostReconcileDatastoreInventoryRequestType from a dict
host_reconcile_datastore_inventory_request_type_form_dict = host_reconcile_datastore_inventory_request_type.from_dict(host_reconcile_datastore_inventory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


