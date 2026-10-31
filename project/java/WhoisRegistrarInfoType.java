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
  A Whois registrar info type is a grouping of characteristics unique to registrar-related information present in a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WhoisRegistrarInfoType extends UcoInherentCharacterizationThing {

  private ObservableObject contactPhoneNumber;
  private ObservableObject emailAddress;
  private Location geolocationAddress;
  private ObservableObject referralURL;
  private String registrarGUID;
  private String registrarID;
  private String registrarName;
  private ObservableObject whoisServer;


}