# OvfConsumerPowerOnFault

A fault type indicating that the power on operation failed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | The OVF consumer&#39;s extension key.  ***Since:*** vSphere API 5.0  | 
**extension_name** | **str** | The OVF consumer&#39;s extension name.  ***Since:*** vSphere API 5.0  | 
**description** | **str** | A localized, human-readable description of the error.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_power_on_fault import OvfConsumerPowerOnFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerPowerOnFault from a JSON string
ovf_consumer_power_on_fault_instance = OvfConsumerPowerOnFault.from_json(json)
# print the JSON string representation of the object
print OvfConsumerPowerOnFault.to_json()

# convert the object into a dict
ovf_consumer_power_on_fault_dict = ovf_consumer_power_on_fault_instance.to_dict()
# create an instance of OvfConsumerPowerOnFault from a dict
ovf_consumer_power_on_fault_form_dict = ovf_consumer_power_on_fault.from_dict(ovf_consumer_power_on_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


