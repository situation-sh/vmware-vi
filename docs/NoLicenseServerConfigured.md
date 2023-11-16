# NoLicenseServerConfigured

The NoLicenseServerConfigured fault is thrown when there is no valid license server configured for the system and the system is not in evaluation mode.  Any operation occurs that requires evaluation license or a valid license will throw the NoLicenseServerConfigured. This can happen with the new licensing scheme that is a hybrid of flex-based licensing and serial number based licensing. There can be cases where VirtualCenter is licensed by a serial number and there is no need for a flex license server. These cases are valid as long as no operation that requires flex- based license server is invoked, for example, adding a pre-4.0 host that requires flex licenses. If however, such an operation is invoked, the NoLicenseServerConfigured fault is thrown.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_license_server_configured import NoLicenseServerConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of NoLicenseServerConfigured from a JSON string
no_license_server_configured_instance = NoLicenseServerConfigured.from_json(json)
# print the JSON string representation of the object
print NoLicenseServerConfigured.to_json()

# convert the object into a dict
no_license_server_configured_dict = no_license_server_configured_instance.to_dict()
# create an instance of NoLicenseServerConfigured from a dict
no_license_server_configured_form_dict = no_license_server_configured.from_dict(no_license_server_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


