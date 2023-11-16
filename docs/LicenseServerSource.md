# LicenseServerSource

Deprecated as of vSphere API 4.0, this is not used by the system.  Specify a license server reachable via IPv4 network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_server** | **str** | This property defines the server to establish a TCP session to obtain license data.  Format of string is host:port Port is optional unsigned 16 bit integer license server is listening on. A trailing colon &#39;:&#39; without a port number is a valid expression. Host can either be an IPv4 address in dotted quad format or a resolvable DNS name &amp;leq;254 characters. See RFC 3696.  | 

## Example

```python
from vmware_vi.models.license_server_source import LicenseServerSource

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseServerSource from a JSON string
license_server_source_instance = LicenseServerSource.from_json(json)
# print the JSON string representation of the object
print LicenseServerSource.to_json()

# convert the object into a dict
license_server_source_dict = license_server_source_instance.to_dict()
# create an instance of LicenseServerSource from a dict
license_server_source_form_dict = license_server_source.from_dict(license_server_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


