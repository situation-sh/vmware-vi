# ArrayOfExtensionOvfConsumerInfo

A boxed array of *ExtensionOvfConsumerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtensionOvfConsumerInfo]**](ExtensionOvfConsumerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extension_ovf_consumer_info import ArrayOfExtensionOvfConsumerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtensionOvfConsumerInfo from a JSON string
array_of_extension_ovf_consumer_info_instance = ArrayOfExtensionOvfConsumerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtensionOvfConsumerInfo.to_json()

# convert the object into a dict
array_of_extension_ovf_consumer_info_dict = array_of_extension_ovf_consumer_info_instance.to_dict()
# create an instance of ArrayOfExtensionOvfConsumerInfo from a dict
array_of_extension_ovf_consumer_info_form_dict = array_of_extension_ovf_consumer_info.from_dict(array_of_extension_ovf_consumer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


