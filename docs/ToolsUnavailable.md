# ToolsUnavailable

A ToolsUnavailableFault exception is thrown when an operation fails to contact VMware Tools running inside the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_unavailable import ToolsUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsUnavailable from a JSON string
tools_unavailable_instance = ToolsUnavailable.from_json(json)
# print the JSON string representation of the object
print ToolsUnavailable.to_json()

# convert the object into a dict
tools_unavailable_dict = tools_unavailable_instance.to_dict()
# create an instance of ToolsUnavailable from a dict
tools_unavailable_form_dict = tools_unavailable.from_dict(tools_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


