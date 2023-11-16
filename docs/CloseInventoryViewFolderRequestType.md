# CloseInventoryViewFolderRequestType

The parameters of *InventoryView.CloseInventoryViewFolder*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | An array of managed object references. Each array entry is a reference to an entity to collapse.  ***Required privileges:*** System.View  Refers instances of *ManagedEntity*.  | 

## Example

```python
from vmware_vi.models.close_inventory_view_folder_request_type import CloseInventoryViewFolderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CloseInventoryViewFolderRequestType from a JSON string
close_inventory_view_folder_request_type_instance = CloseInventoryViewFolderRequestType.from_json(json)
# print the JSON string representation of the object
print CloseInventoryViewFolderRequestType.to_json()

# convert the object into a dict
close_inventory_view_folder_request_type_dict = close_inventory_view_folder_request_type_instance.to_dict()
# create an instance of CloseInventoryViewFolderRequestType from a dict
close_inventory_view_folder_request_type_form_dict = close_inventory_view_folder_request_type.from_dict(close_inventory_view_folder_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


