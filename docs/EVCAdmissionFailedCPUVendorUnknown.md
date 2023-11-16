# EVCAdmissionFailedCPUVendorUnknown

The host's CPU vendor is unknown, which prevents admission into an Enhanced VMotion Compatibility cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.evc_admission_failed_cpu_vendor_unknown import EVCAdmissionFailedCPUVendorUnknown

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedCPUVendorUnknown from a JSON string
evc_admission_failed_cpu_vendor_unknown_instance = EVCAdmissionFailedCPUVendorUnknown.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedCPUVendorUnknown.to_json()

# convert the object into a dict
evc_admission_failed_cpu_vendor_unknown_dict = evc_admission_failed_cpu_vendor_unknown_instance.to_dict()
# create an instance of EVCAdmissionFailedCPUVendorUnknown from a dict
evc_admission_failed_cpu_vendor_unknown_form_dict = evc_admission_failed_cpu_vendor_unknown.from_dict(evc_admission_failed_cpu_vendor_unknown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


