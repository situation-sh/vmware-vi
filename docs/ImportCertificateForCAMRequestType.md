# ImportCertificateForCAMRequestType

The parameters of *HostActiveDirectoryAuthentication.ImportCertificateForCAM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_path** | **str** | full path of the certificate on ESXi  | 
**cam_server** | **str** | IP of server providing the CAM service.  | 

## Example

```python
from vmware_vi.models.import_certificate_for_cam_request_type import ImportCertificateForCAMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCertificateForCAMRequestType from a JSON string
import_certificate_for_cam_request_type_instance = ImportCertificateForCAMRequestType.from_json(json)
# print the JSON string representation of the object
print ImportCertificateForCAMRequestType.to_json()

# convert the object into a dict
import_certificate_for_cam_request_type_dict = import_certificate_for_cam_request_type_instance.to_dict()
# create an instance of ImportCertificateForCAMRequestType from a dict
import_certificate_for_cam_request_type_form_dict = import_certificate_for_cam_request_type.from_dict(import_certificate_for_cam_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


