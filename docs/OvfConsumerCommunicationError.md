# OvfConsumerCommunicationError

A fault type indicating that network communication with an OVF consumer failed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The network library error message.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_communication_error import OvfConsumerCommunicationError

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerCommunicationError from a JSON string
ovf_consumer_communication_error_instance = OvfConsumerCommunicationError.from_json(json)
# print the JSON string representation of the object
print OvfConsumerCommunicationError.to_json()

# convert the object into a dict
ovf_consumer_communication_error_dict = ovf_consumer_communication_error_instance.to_dict()
# create an instance of OvfConsumerCommunicationError from a dict
ovf_consumer_communication_error_form_dict = ovf_consumer_communication_error.from_dict(ovf_consumer_communication_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


