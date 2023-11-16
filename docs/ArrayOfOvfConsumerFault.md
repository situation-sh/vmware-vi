# ArrayOfOvfConsumerFault

A boxed array of *OvfConsumerFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfConsumerFault]**](OvfConsumerFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_consumer_fault import ArrayOfOvfConsumerFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfConsumerFault from a JSON string
array_of_ovf_consumer_fault_instance = ArrayOfOvfConsumerFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfConsumerFault.to_json()

# convert the object into a dict
array_of_ovf_consumer_fault_dict = array_of_ovf_consumer_fault_instance.to_dict()
# create an instance of ArrayOfOvfConsumerFault from a dict
array_of_ovf_consumer_fault_form_dict = array_of_ovf_consumer_fault.from_dict(array_of_ovf_consumer_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


