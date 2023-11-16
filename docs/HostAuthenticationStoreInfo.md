# HostAuthenticationStoreInfo

The *HostAuthenticationStoreInfo* base class defines status information for local and host Active Directory authentication.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the authentication store is configured. - Host Active Directory authentication - &lt;code&gt;enabled&lt;/code&gt;   is &lt;code&gt;True&lt;/code&gt; if the host is a member of a domain. - Local authentication - &lt;code&gt;enabled&lt;/code&gt; is always &lt;code&gt;True&lt;/code&gt;.    ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.host_authentication_store_info import HostAuthenticationStoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostAuthenticationStoreInfo from a JSON string
host_authentication_store_info_instance = HostAuthenticationStoreInfo.from_json(json)
# print the JSON string representation of the object
print HostAuthenticationStoreInfo.to_json()

# convert the object into a dict
host_authentication_store_info_dict = host_authentication_store_info_instance.to_dict()
# create an instance of HostAuthenticationStoreInfo from a dict
host_authentication_store_info_form_dict = host_authentication_store_info.from_dict(host_authentication_store_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


