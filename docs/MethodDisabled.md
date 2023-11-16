# MethodDisabled

A MethodDisabled fault is thrown if a disabled method is invoked by the client.  The method denote an invalid state operation or may have been explicitly disabled.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.method_disabled import MethodDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of MethodDisabled from a JSON string
method_disabled_instance = MethodDisabled.from_json(json)
# print the JSON string representation of the object
print MethodDisabled.to_json()

# convert the object into a dict
method_disabled_dict = method_disabled_instance.to_dict()
# create an instance of MethodDisabled from a dict
method_disabled_form_dict = method_disabled.from_dict(method_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


