class Spotter():
    """
    The Spotter interface to be implemented

    Attributes
    ----------
    uid : str
        uid of the spotter
    hashSpotted : bool, optional
        False by default, whether to hash or replace the spotted sensitive information

    Methods
    -------
    getSpotterUID()
        return the Spotter uid
    
    isHashSpotted()
        return whether the hashSpotted is True or False
    
    process(text)
        process the text depending on the hashSpotted value, if it is hash, replace it with hash
        otherwise, replace it with some default value
    """
    # please add the following line in the subclass
    # spotter_uid = "<uid of the spotter>"
    def __init__(self, uid: str, hashSpotted=False):
        self.uid = uid
        self.hashSpotted = hashSpotted

    def getSpotterUID(self) -> str:
        """Getting the spotter uid

        Returns
        -------
        self.uid : str
            the spotter uid
        """
        return self.uid

    def isHashSpotted(self) -> bool:
        """Getting the value of hashSpotted

        Returns
        -------
        self.hashSpotted : bool
            the Truth value of hashSpotted
        """
        return self.hashSpotted

    def process(self, text: str) -> str:
        """Process the given text, if hashSpotted is True, replace the spotted text with hash,
        otherwise, replace the spotted text with some default values
        
        Parameters
        ----------
        text : str
            The text to be spotted & modified

        Returns
        -------
        new_text : str
            
        """
        # # to be implemented in the specific spotter level
        # if self.isHashSpotted():
        #     new_text = "hash"
        # else:
        #     new_text = ""
        # return new_text
        pass
