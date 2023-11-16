# OpenInventoryViewFolderRequestType

The parameters of *InventoryView.OpenInventoryViewFolder*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | An array of managed object references. Each array entry is a reference to an entity to expand. Expands each entity in the order given. If an entity is not in the current view, expands the view as needed.  ***Required privileges:*** System.View  Refers instances of *ManagedEntity*.  | 

## Example

```python
from vmware_vi.models.open_inventory_view_folder_request_type import OpenInventoryViewFolderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of OpenInventoryViewFolderRequestType from a JSON string
open_inventory_view_folder_request_type_instance = OpenInventoryViewFolderRequestType.from_json(json)
# print the JSON string representation of the object
print OpenInventoryViewFolderRequestType.to_json()

# convert the object into a dict
open_inventory_view_folder_request_type_dict = open_inventory_view_folder_request_type_instance.to_dict()
# create an instance of OpenInventoryViewFolderRequestType from a dict
open_inventory_view_folder_request_type_form_dict = open_inventory_view_folder_request_type.from_dict(open_inventory_view_folder_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


