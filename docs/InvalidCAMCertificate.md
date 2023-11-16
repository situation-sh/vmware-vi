# InvalidCAMCertificate

Fault indicating that the CAM server's certificate cannot be verified.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_cam_certificate import InvalidCAMCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidCAMCertificate from a JSON string
invalid_cam_certificate_instance = InvalidCAMCertificate.from_json(json)
# print the JSON string representation of the object
print InvalidCAMCertificate.to_json()

# convert the object into a dict
invalid_cam_certificate_dict = invalid_cam_certificate_instance.to_dict()
# create an instance of InvalidCAMCertificate from a dict
invalid_cam_certificate_form_dict = invalid_cam_certificate.from_dict(invalid_cam_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


