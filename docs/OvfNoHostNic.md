# OvfNoHostNic

This fault is used if there is no network defined on host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_no_host_nic import OvfNoHostNic

# TODO update the JSON string below
json = "{}"
# create an instance of OvfNoHostNic from a JSON string
ovf_no_host_nic_instance = OvfNoHostNic.from_json(json)
# print the JSON string representation of the object
print OvfNoHostNic.to_json()

# convert the object into a dict
ovf_no_host_nic_dict = ovf_no_host_nic_instance.to_dict()
# create an instance of OvfNoHostNic from a dict
ovf_no_host_nic_form_dict = ovf_no_host_nic.from_dict(ovf_no_host_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


