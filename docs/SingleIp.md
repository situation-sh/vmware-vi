# SingleIp

This class specifies a single IP address.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address.  The value of this property should either be an IPv4 address such as \&quot;192.168.0.1\&quot; or an IPv6 address such as \&quot;fc00:192:168:0:6cd9:a132:e889:b612\&quot;  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.single_ip import SingleIp

# TODO update the JSON string below
json = "{}"
# create an instance of SingleIp from a JSON string
single_ip_instance = SingleIp.from_json(json)
# print the JSON string representation of the object
print SingleIp.to_json()

# convert the object into a dict
single_ip_dict = single_ip_instance.to_dict()
# create an instance of SingleIp from a dict
single_ip_form_dict = single_ip.from_dict(single_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


