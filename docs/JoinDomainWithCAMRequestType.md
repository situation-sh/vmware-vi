# JoinDomainWithCAMRequestType

The parameters of *HostActiveDirectoryAuthentication.JoinDomainWithCAM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Name of the domain to be joined.  | 
**cam_server** | **str** | Name of server providing the CAM service.  | 

## Example

```python
from vmware_vi.models.join_domain_with_cam_request_type import JoinDomainWithCAMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of JoinDomainWithCAMRequestType from a JSON string
join_domain_with_cam_request_type_instance = JoinDomainWithCAMRequestType.from_json(json)
# print the JSON string representation of the object
print JoinDomainWithCAMRequestType.to_json()

# convert the object into a dict
join_domain_with_cam_request_type_dict = join_domain_with_cam_request_type_instance.to_dict()
# create an instance of JoinDomainWithCAMRequestType from a dict
join_domain_with_cam_request_type_form_dict = join_domain_with_cam_request_type.from_dict(join_domain_with_cam_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


