# EVCAdmissionFailedVmActive

An attempt to move or add a host into an Enhanced VMotion Compatibility cluster has failed for the following reason: - The host exposes additional compatibility-relevant CPU features beyond   those present in the baseline mandated by the cluster's EVC mode. - The host has powered-on or suspended virtual machines.    Therefore the host may not be admitted into the cluster, since its virtual machines may be using CPU features suppressed in the cluster.  Note that in rare cases, this may occur even if the host's *maxEVCModeKey* corresponds to the EVC mode of the cluster. This means that even though that EVC mode is the best match for the host's hardware, the host still has some features beyond those present in the baseline for that EVC mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_vm_active import EVCAdmissionFailedVmActive

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedVmActive from a JSON string
evc_admission_failed_vm_active_instance = EVCAdmissionFailedVmActive.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedVmActive.to_json()

# convert the object into a dict
evc_admission_failed_vm_active_dict = evc_admission_failed_vm_active_instance.to_dict()
# create an instance of EVCAdmissionFailedVmActive from a dict
evc_admission_failed_vm_active_form_dict = evc_admission_failed_vm_active.from_dict(evc_admission_failed_vm_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


