# CreateListViewRequestType

The parameters of *ViewManager.CreateListView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The initial list of objects in the view.  ***Required privileges:*** System.View  | [optional] 

## Example

```python
from vmware_vi.models.create_list_view_request_type import CreateListViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListViewRequestType from a JSON string
create_list_view_request_type_instance = CreateListViewRequestType.from_json(json)
# print the JSON string representation of the object
print CreateListViewRequestType.to_json()

# convert the object into a dict
create_list_view_request_type_dict = create_list_view_request_type_instance.to_dict()
# create an instance of CreateListViewRequestType from a dict
create_list_view_request_type_form_dict = create_list_view_request_type.from_dict(create_list_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


