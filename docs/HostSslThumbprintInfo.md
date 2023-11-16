# HostSslThumbprintInfo

The SSL thumbprint information for a host managed by a vCenter Server or a vCenter extension to login into other hosts without username/password authentication.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | The principal used for the login session  ***Since:*** vSphere API 4.0  | 
**owner_tag** | **str** | The tag associated with this registration.  Owner tags allow multiple entities to register the same thumbprint without interfering with each other on the life cycle of the thumbprint with their unique tags. Each solution should use a unique tag to identify itself.  ***Since:*** vSphere API 5.0  | 
**ssl_thumbprints** | **List[str]** | Specify the SSL thumbprints to register on the host.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ssl_thumbprint_info import HostSslThumbprintInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSslThumbprintInfo from a JSON string
host_ssl_thumbprint_info_instance = HostSslThumbprintInfo.from_json(json)
# print the JSON string representation of the object
print HostSslThumbprintInfo.to_json()

# convert the object into a dict
host_ssl_thumbprint_info_dict = host_ssl_thumbprint_info_instance.to_dict()
# create an instance of HostSslThumbprintInfo from a dict
host_ssl_thumbprint_info_form_dict = host_ssl_thumbprint_info.from_dict(host_ssl_thumbprint_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


