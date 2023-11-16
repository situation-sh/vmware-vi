# OvfConsumerValidationFault

Thrown by an OVF consumer if an error occurred while validating an instantiation OST.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | The OVF consumer&#39;s extension key.  ***Since:*** vSphere API 5.0  | 
**extension_name** | **str** | The OVF consumer&#39;s extension name.  ***Since:*** vSphere API 5.0  | 
**message** | **str** | The error message, localized by the OVF consumer  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_validation_fault import OvfConsumerValidationFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerValidationFault from a JSON string
ovf_consumer_validation_fault_instance = OvfConsumerValidationFault.from_json(json)
# print the JSON string representation of the object
print OvfConsumerValidationFault.to_json()

# convert the object into a dict
ovf_consumer_validation_fault_dict = ovf_consumer_validation_fault_instance.to_dict()
# create an instance of OvfConsumerValidationFault from a dict
ovf_consumer_validation_fault_form_dict = ovf_consumer_validation_fault.from_dict(ovf_consumer_validation_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


