# HostActiveDirectorySpec

The *HostActiveDirectorySpec* data object defines properties for Active Directory domain access.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Domain name.  ***Since:*** vSphere API 4.1  | [optional] 
**user_name** | **str** | Name of an Active Directory account with the authority to add a host to the domain.  ***Since:*** vSphere API 4.1  | [optional] 
**password** | **str** | Password for the Active Directory account.  ***Since:*** vSphere API 4.1  | [optional] 
**cam_server** | **str** | If set, the CAM server will be used to join the domain and the &lt;code&gt;userName&lt;/code&gt; and &lt;code&gt;password&lt;/code&gt; fields will be ignored.  ***Since:*** vSphere API 5.0  | [optional] 
**thumbprint** | **str** | Thumbprint for the SSL certficate of CAM server  ***Since:*** vSphere API 5.0  | [optional] 
**smart_card_authentication_enabled** | **bool** | Support smart card authentication of local users.  ***Since:*** vSphere API 6.0  | [optional] 
**smart_card_trust_anchors** | **List[str]** | Trusted root certificates for smart cards.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_active_directory_spec import HostActiveDirectorySpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostActiveDirectorySpec from a JSON string
host_active_directory_spec_instance = HostActiveDirectorySpec.from_json(json)
# print the JSON string representation of the object
print HostActiveDirectorySpec.to_json()

# convert the object into a dict
host_active_directory_spec_dict = host_active_directory_spec_instance.to_dict()
# create an instance of HostActiveDirectorySpec from a dict
host_active_directory_spec_form_dict = host_active_directory_spec.from_dict(host_active_directory_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


