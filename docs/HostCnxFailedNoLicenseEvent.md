# HostCnxFailedNoLicenseEvent

This event records a failure to connect to a host due to a licensing issue. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_no_license_event import HostCnxFailedNoLicenseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedNoLicenseEvent from a JSON string
host_cnx_failed_no_license_event_instance = HostCnxFailedNoLicenseEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedNoLicenseEvent.to_json()

# convert the object into a dict
host_cnx_failed_no_license_event_dict = host_cnx_failed_no_license_event_instance.to_dict()
# create an instance of HostCnxFailedNoLicenseEvent from a dict
host_cnx_failed_no_license_event_form_dict = host_cnx_failed_no_license_event.from_dict(host_cnx_failed_no_license_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


