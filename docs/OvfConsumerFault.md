# OvfConsumerFault

Localized fault that may be thrown by an OVF consumer.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_key** | **str** | An error code that uniquely describes the fault within this extension.  ***Since:*** vSphere API 5.0  | 
**message** | **str** | The error message, localized by the OVF consumer  ***Since:*** vSphere API 5.0  | 
**params** | [**List[KeyValue]**](KeyValue.md) | Additional parameters for this fault  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_consumer_fault import OvfConsumerFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerFault from a JSON string
ovf_consumer_fault_instance = OvfConsumerFault.from_json(json)
# print the JSON string representation of the object
print OvfConsumerFault.to_json()

# convert the object into a dict
ovf_consumer_fault_dict = ovf_consumer_fault_instance.to_dict()
# create an instance of OvfConsumerFault from a dict
ovf_consumer_fault_form_dict = ovf_consumer_fault.from_dict(ovf_consumer_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


