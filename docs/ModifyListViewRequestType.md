# ModifyListViewRequestType

The parameters of *ListView.ModifyListView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Optional list of objects to add to the view.  ***Required privileges:*** System.View  | [optional] 
**remove** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Optional list of objects to remove from the view.  ***Required privileges:*** System.View  | [optional] 

## Example

```python
from vmware_vi.models.modify_list_view_request_type import ModifyListViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyListViewRequestType from a JSON string
modify_list_view_request_type_instance = ModifyListViewRequestType.from_json(json)
# print the JSON string representation of the object
print ModifyListViewRequestType.to_json()

# convert the object into a dict
modify_list_view_request_type_dict = modify_list_view_request_type_instance.to_dict()
# create an instance of ModifyListViewRequestType from a dict
modify_list_view_request_type_form_dict = modify_list_view_request_type.from_dict(modify_list_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


