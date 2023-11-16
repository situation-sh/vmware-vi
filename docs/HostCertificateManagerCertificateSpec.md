# HostCertificateManagerCertificateSpec

Represents certificate specification used for identifying a specific certificate supported by Host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The list of supported values can be found in *HostCertificateManagerCertificateKind_enum*  | 

## Example

```python
from vmware_vi.models.host_certificate_manager_certificate_spec import HostCertificateManagerCertificateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostCertificateManagerCertificateSpec from a JSON string
host_certificate_manager_certificate_spec_instance = HostCertificateManagerCertificateSpec.from_json(json)
# print the JSON string representation of the object
print HostCertificateManagerCertificateSpec.to_json()

# convert the object into a dict
host_certificate_manager_certificate_spec_dict = host_certificate_manager_certificate_spec_instance.to_dict()
# create an instance of HostCertificateManagerCertificateSpec from a dict
host_certificate_manager_certificate_spec_form_dict = host_certificate_manager_certificate_spec.from_dict(host_certificate_manager_certificate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


