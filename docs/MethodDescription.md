# MethodDescription

Static strings used for describing an object model method. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Method being described.  | 

## Example

```python
from vmware_vi.models.method_description import MethodDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MethodDescription from a JSON string
method_description_instance = MethodDescription.from_json(json)
# print the JSON string representation of the object
print MethodDescription.to_json()

# convert the object into a dict
method_description_dict = method_description_instance.to_dict()
# create an instance of MethodDescription from a dict
method_description_form_dict = method_description.from_dict(method_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


