# BlockedByFirewall

Fault indicating that firewall configuration prevents an operation from completing successfully.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.blocked_by_firewall import BlockedByFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of BlockedByFirewall from a JSON string
blocked_by_firewall_instance = BlockedByFirewall.from_json(json)
# print the JSON string representation of the object
print BlockedByFirewall.to_json()

# convert the object into a dict
blocked_by_firewall_dict = blocked_by_firewall_instance.to_dict()
# create an instance of BlockedByFirewall from a dict
blocked_by_firewall_form_dict = blocked_by_firewall.from_dict(blocked_by_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


