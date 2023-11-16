# VspanPromiscuousPortNotSupported

Thrown if a promiscuous port appears in transmitted source or destination ports of any Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session_key** | **str** | The key of the Distributed Port Mirroring session in which a promiscuous port is used as transmitted source or destination ports.  ***Since:*** vSphere API 5.0  | 
**port_key** | **str** | The key of the promiscuous port that appears in transmitted source or destination ports.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_promiscuous_port_not_supported import VspanPromiscuousPortNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPromiscuousPortNotSupported from a JSON string
vspan_promiscuous_port_not_supported_instance = VspanPromiscuousPortNotSupported.from_json(json)
# print the JSON string representation of the object
print VspanPromiscuousPortNotSupported.to_json()

# convert the object into a dict
vspan_promiscuous_port_not_supported_dict = vspan_promiscuous_port_not_supported_instance.to_dict()
# create an instance of VspanPromiscuousPortNotSupported from a dict
vspan_promiscuous_port_not_supported_form_dict = vspan_promiscuous_port_not_supported.from_dict(vspan_promiscuous_port_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


