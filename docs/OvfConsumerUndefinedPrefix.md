# OvfConsumerUndefinedPrefix

A fault type indicating that an OVF consumer added a section with an unbound prefix.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The prefix for which no namespace definition was found.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_undefined_prefix import OvfConsumerUndefinedPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerUndefinedPrefix from a JSON string
ovf_consumer_undefined_prefix_instance = OvfConsumerUndefinedPrefix.from_json(json)
# print the JSON string representation of the object
print OvfConsumerUndefinedPrefix.to_json()

# convert the object into a dict
ovf_consumer_undefined_prefix_dict = ovf_consumer_undefined_prefix_instance.to_dict()
# create an instance of OvfConsumerUndefinedPrefix from a dict
ovf_consumer_undefined_prefix_form_dict = ovf_consumer_undefined_prefix.from_dict(ovf_consumer_undefined_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


