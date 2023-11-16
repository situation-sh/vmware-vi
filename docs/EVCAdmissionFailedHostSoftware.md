# EVCAdmissionFailedHostSoftware

The host's software does not support any Enhanced VMotion Compatibility mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_host_software import EVCAdmissionFailedHostSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedHostSoftware from a JSON string
evc_admission_failed_host_software_instance = EVCAdmissionFailedHostSoftware.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedHostSoftware.to_json()

# convert the object into a dict
evc_admission_failed_host_software_dict = evc_admission_failed_host_software_instance.to_dict()
# create an instance of EVCAdmissionFailedHostSoftware from a dict
evc_admission_failed_host_software_form_dict = evc_admission_failed_host_software.from_dict(evc_admission_failed_host_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


