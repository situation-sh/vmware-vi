# EVCAdmissionFailedHostSoftwareForMode

The host's software does not support the Enhanced VMotion Compatibility mode of the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_host_software_for_mode import EVCAdmissionFailedHostSoftwareForMode

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedHostSoftwareForMode from a JSON string
evc_admission_failed_host_software_for_mode_instance = EVCAdmissionFailedHostSoftwareForMode.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedHostSoftwareForMode.to_json()

# convert the object into a dict
evc_admission_failed_host_software_for_mode_dict = evc_admission_failed_host_software_for_mode_instance.to_dict()
# create an instance of EVCAdmissionFailedHostSoftwareForMode from a dict
evc_admission_failed_host_software_for_mode_form_dict = evc_admission_failed_host_software_for_mode.from_dict(evc_admission_failed_host_software_for_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


