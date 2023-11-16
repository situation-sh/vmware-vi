# OvfConsumerCallbackFault

Superclass for all faults that can be thrown during the callback to an OVF consumer.  The *MethodFault.faultCause* gives details about what went wrong.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | The OVF consumer&#39;s extension key.  ***Since:*** vSphere API 5.0  | 
**extension_name** | **str** | The OVF consumer&#39;s extension name.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_callback_fault import OvfConsumerCallbackFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerCallbackFault from a JSON string
ovf_consumer_callback_fault_instance = OvfConsumerCallbackFault.from_json(json)
# print the JSON string representation of the object
print OvfConsumerCallbackFault.to_json()

# convert the object into a dict
ovf_consumer_callback_fault_dict = ovf_consumer_callback_fault_instance.to_dict()
# create an instance of OvfConsumerCallbackFault from a dict
ovf_consumer_callback_fault_form_dict = ovf_consumer_callback_fault.from_dict(ovf_consumer_callback_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


