# OvfPropertyNetwork

A class used indicate there was a property network error  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_property_network import OvfPropertyNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyNetwork from a JSON string
ovf_property_network_instance = OvfPropertyNetwork.from_json(json)
# print the JSON string representation of the object
print OvfPropertyNetwork.to_json()

# convert the object into a dict
ovf_property_network_dict = ovf_property_network_instance.to_dict()
# create an instance of OvfPropertyNetwork from a dict
ovf_property_network_form_dict = ovf_property_network.from_dict(ovf_property_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


