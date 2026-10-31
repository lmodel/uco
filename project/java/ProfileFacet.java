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
  A profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single user account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileFacet extends Facet {

  private ContactAddress contactAddress;
  private ContactEmail contactEmail;
  private ContactMessaging contactMessaging;
  private ContactPhone contactPhone;
  private ContactURL contactURL;
  private String displayName;
  private String name;
  private ObservableObject profileAccount;
  private ZonedDateTime profileCreated;
  private Identity profileIdentity;
  private List<String> profileLanguage;
  private ObservableObject profileService;
  private ObservableObject profileWebsite;


}