package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A whois facet is a grouping of characteristics unique to a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WhoIsFacet extends Facet {

  private ZonedDateTime creationDate;
  private String dnssec;
  private String domainID;
  private ObservableObject domainName;
  private ZonedDateTime expirationDate;
  private ObservableObject ipAddress;
  private ZonedDateTime lookupDate;
  private List<ObservableObject> nameServer;
  private String regionalInternetRegistry;
  private ObservableObject registrantContactInfo;
  private List<String> registrantIDs;
  private WhoisRegistrarInfoType registrarInfo;
  private String remarks;
  private ObservableObject serverName;
  private String sponsoringRegistrar;
  private String status;
  private ZonedDateTime updatedDate;


}