# InsufficientGraphicsResourcesFault

Graphics resources admission control failed  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_graphics_resources_fault import InsufficientGraphicsResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientGraphicsResourcesFault from a JSON string
insufficient_graphics_resources_fault_instance = InsufficientGraphicsResourcesFault.from_json(json)
# print the JSON string representation of the object
print InsufficientGraphicsResourcesFault.to_json()

# convert the object into a dict
insufficient_graphics_resources_fault_dict = insufficient_graphics_resources_fault_instance.to_dict()
# create an instance of InsufficientGraphicsResourcesFault from a dict
insufficient_graphics_resources_fault_form_dict = insufficient_graphics_resources_fault.from_dict(insufficient_graphics_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


