# NoVcManagedIpConfigured

The IP address of the VC server has not be configured, and a vApp property is requesting to use it.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_vc_managed_ip_configured import NoVcManagedIpConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of NoVcManagedIpConfigured from a JSON string
no_vc_managed_ip_configured_instance = NoVcManagedIpConfigured.from_json(json)
# print the JSON string representation of the object
print NoVcManagedIpConfigured.to_json()

# convert the object into a dict
no_vc_managed_ip_configured_dict = no_vc_managed_ip_configured_instance.to_dict()
# create an instance of NoVcManagedIpConfigured from a dict
no_vc_managed_ip_configured_form_dict = no_vc_managed_ip_configured.from_dict(no_vc_managed_ip_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


