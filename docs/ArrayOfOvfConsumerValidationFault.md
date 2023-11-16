# ArrayOfOvfConsumerValidationFault

A boxed array of *OvfConsumerValidationFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfConsumerValidationFault]**](OvfConsumerValidationFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_consumer_validation_fault import ArrayOfOvfConsumerValidationFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfConsumerValidationFault from a JSON string
array_of_ovf_consumer_validation_fault_instance = ArrayOfOvfConsumerValidationFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfConsumerValidationFault.to_json()

# convert the object into a dict
array_of_ovf_consumer_validation_fault_dict = array_of_ovf_consumer_validation_fault_instance.to_dict()
# create an instance of ArrayOfOvfConsumerValidationFault from a dict
array_of_ovf_consumer_validation_fault_form_dict = array_of_ovf_consumer_validation_fault.from_dict(array_of_ovf_consumer_validation_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


