# EVCAdmissionFailedCPUVendor

The host's CPU vendor does not match the required CPU vendor for the Enhanced VMotion Compatibility mode of the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_cpu_vendor** | **str** | The CPU vendor required for entering the cluster.  ***Since:*** vSphere API 4.0  | 
**host_cpu_vendor** | **str** | The CPU vendor of the host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.evc_admission_failed_cpu_vendor import EVCAdmissionFailedCPUVendor

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailedCPUVendor from a JSON string
evc_admission_failed_cpu_vendor_instance = EVCAdmissionFailedCPUVendor.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailedCPUVendor.to_json()

# convert the object into a dict
evc_admission_failed_cpu_vendor_dict = evc_admission_failed_cpu_vendor_instance.to_dict()
# create an instance of EVCAdmissionFailedCPUVendor from a dict
evc_admission_failed_cpu_vendor_form_dict = evc_admission_failed_cpu_vendor.from_dict(evc_admission_failed_cpu_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


