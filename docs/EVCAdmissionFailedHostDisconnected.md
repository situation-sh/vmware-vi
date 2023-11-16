# EVCAdmissionFailedHostDisconnected

The host is not connected, which prevents admission into an Enhanced VMotion Compatibility cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_host_disconnected import EVCAdmissionFailedHostDisconnected

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedHostDisconnected from a JSON string
evc_admission_failed_host_disconnected_instance = EVCAdmissionFailedHostDisconnected.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedHostDisconnected.to_json()

# convert the object into a dict
evc_admission_failed_host_disconnected_dict = evc_admission_failed_host_disconnected_instance.to_dict()
# create an instance of EVCAdmissionFailedHostDisconnected from a dict
evc_admission_failed_host_disconnected_form_dict = evc_admission_failed_host_disconnected.from_dict(evc_admission_failed_host_disconnected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


