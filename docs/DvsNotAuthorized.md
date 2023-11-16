# DvsNotAuthorized

Thrown if *DVSCapability.dvsOperationSupported* is false and *DVSConfigInfo.extensionKey* is not same as the extension key of the login-session.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_extension_key** | **str** | The extension key associated with the user-session.  ***Since:*** vSphere API 4.0  | [optional] 
**dvs_extension_key** | **str** | The value of *DVSConfigInfo.extensionKey*.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_not_authorized import DvsNotAuthorized

# TODO update the JSON string below
json = "{}"
# create an instance of DvsNotAuthorized from a JSON string
dvs_not_authorized_instance = DvsNotAuthorized.from_json(json)
# print the JSON string representation of the object
print DvsNotAuthorized.to_json()

# convert the object into a dict
dvs_not_authorized_dict = dvs_not_authorized_instance.to_dict()
# create an instance of DvsNotAuthorized from a dict
dvs_not_authorized_form_dict = dvs_not_authorized.from_dict(dvs_not_authorized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


