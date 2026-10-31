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
  A twitter profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single Twitter user account. [based on https://en.wikipedia.org/wiki/User_profile]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TwitterProfileFacet extends Facet {

  private Integer favoritesCount;
  private Integer followersCount;
  private Integer friendsCount;
  private Integer listedCount;
  private List<Hash> profileBackgroundHash;
  private ObservableObject profileBackgroundLocation;
  private List<Hash> profileBannerHash;
  private ObservableObject profileBannerLocation;
  private List<Hash> profileImageHash;
  private ObservableObject profileImageLocation;
  private Boolean profileIsProtected;
  private Boolean profileIsVerified;
  private Integer statusesCount;
  private String twitterHandle;
  private String twitterId;
  private String userLocationString;


}