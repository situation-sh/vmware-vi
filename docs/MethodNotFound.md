# MethodNotFound

MethodNotFound is thrown to indicate that a method called on a managed object does not exist. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**method** | **str** | The method called.  | 

## Example

```python
from vmware_vi.models.method_not_found import MethodNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MethodNotFound from a JSON string
method_not_found_instance = MethodNotFound.from_json(json)
# print the JSON string representation of the object
print MethodNotFound.to_json()

# convert the object into a dict
method_not_found_dict = method_not_found_instance.to_dict()
# create an instance of MethodNotFound from a dict
method_not_found_form_dict = method_not_found.from_dict(method_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


