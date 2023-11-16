# ReconcileDatastoreInventoryRequestType

The parameters of *VcenterVStorageObjectManager.ReconcileDatastoreInventory_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.reconcile_datastore_inventory_request_type import ReconcileDatastoreInventoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconcileDatastoreInventoryRequestType from a JSON string
reconcile_datastore_inventory_request_type_instance = ReconcileDatastoreInventoryRequestType.from_json(json)
# print the JSON string representation of the object
print ReconcileDatastoreInventoryRequestType.to_json()

# convert the object into a dict
reconcile_datastore_inventory_request_type_dict = reconcile_datastore_inventory_request_type_instance.to_dict()
# create an instance of ReconcileDatastoreInventoryRequestType from a dict
reconcile_datastore_inventory_request_type_form_dict = reconcile_datastore_inventory_request_type.from_dict(reconcile_datastore_inventory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


