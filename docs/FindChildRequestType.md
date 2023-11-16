# FindChildRequestType

The parameters of *SearchIndex.FindChild*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | The name of the child object.  | 

## Example

```python
from vmware_vi.models.find_child_request_type import FindChildRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindChildRequestType from a JSON string
find_child_request_type_instance = FindChildRequestType.from_json(json)
# print the JSON string representation of the object
print FindChildRequestType.to_json()

# convert the object into a dict
find_child_request_type_dict = find_child_request_type_instance.to_dict()
# create an instance of FindChildRequestType from a dict
find_child_request_type_form_dict = find_child_request_type.from_dict(find_child_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


