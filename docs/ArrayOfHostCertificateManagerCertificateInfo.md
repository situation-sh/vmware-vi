# ArrayOfHostCertificateManagerCertificateInfo

A boxed array of *HostCertificateManagerCertificateInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCertificateManagerCertificateInfo]**](HostCertificateManagerCertificateInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_certificate_manager_certificate_info import ArrayOfHostCertificateManagerCertificateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCertificateManagerCertificateInfo from a JSON string
array_of_host_certificate_manager_certificate_info_instance = ArrayOfHostCertificateManagerCertificateInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCertificateManagerCertificateInfo.to_json()

# convert the object into a dict
array_of_host_certificate_manager_certificate_info_dict = array_of_host_certificate_manager_certificate_info_instance.to_dict()
# create an instance of ArrayOfHostCertificateManagerCertificateInfo from a dict
array_of_host_certificate_manager_certificate_info_form_dict = array_of_host_certificate_manager_certificate_info.from_dict(array_of_host_certificate_manager_certificate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


